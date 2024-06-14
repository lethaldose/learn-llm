import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.globals import set_debug
import dotenv
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

dotenv.load_dotenv()

set_debug(True)

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

# Load, chunk and index the contents of the blog.
loader = WebBaseLoader(
    web_paths=("https://medium.com/technogise/building-a-low-maintenance-software-a7f4cf758930",),
    # bs_kwargs=dict(
    #     parse_only=bs4.SoupStrainer(
    #         class_=("post-content", "post-title", "post-header")
    #     )
    # ),
)
docs = loader.load()

print(len(docs[0].page_content))
print(docs[0].page_content[:100])

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

print('Length of splits', len(splits))
print('Length of 1st split', len(splits[0].page_content))
print('Metadata of last split', splits[3].metadata)

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_function)

# query it
query = "What is the plumbing crisis?"
found_docs = vectorstore.similarity_search(query)

# print results
print(found_docs[0].page_content)

# Retrieve and generate using the relevant snippets of the blog.
# retriever = vectorstore.as_retriever()
# prompt = hub.pull("rlm/rag-prompt")
#
#
# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)
#
#
# rag_chain = (
#         {"context": retriever | format_docs, "question": RunnablePassthrough()}
#         | prompt
#         | llm
#         | StrOutputParser()
# )
#
# rag_chain.invoke("What is oracle wallet?")

# cleanup
vectorstore.delete_collection()
