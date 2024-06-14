-- https://github.com/pgvector/pgvector
-- in psql command line:
-- CREATE EXTENSION vector;

CREATE TABLE
  documents (
    id bigint PRIMARY KEY,
    created_at timestamp
    with
      time zone,
      content text,
      embedding public.vector (3)
  );

INSERT INTO
  documents (created_at, content, embedding)
VALUES
  ('2023-06-01 00:00:00', 'the quick', '[1,2,3]'),
  ('2023-06-02 00:00:00', 'brown fox', '[4,5,6]'),
  ('2023-06-03 00:00:00', 'jumped over' '[7,8,9]');

-- Supported distance functions are:
-- <-> - L2 distance
-- <#> - (negative) inner product
-- <=> - cosine distance
-- <+> - L1 distance (added in 0.7.0)

select *, embedding <-> '[4,5,7]'::vector as similarity from documents;
select *, embedding <=> '[4,5,7]'::vector as similarity from documents;
