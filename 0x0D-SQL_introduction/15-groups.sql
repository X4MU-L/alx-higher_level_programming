-- Lists all records of the table second_table of the database
   -- * Don't list records without a name.
   -- * Results should display the score and the name
   -- * Record should be listed by descending score.
SELECT score, count(score) as number FROM second_table ORDER BY score DESC;
