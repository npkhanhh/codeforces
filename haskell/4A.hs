main = do
    a <- readLn
    putStrLn $ if even a && a > 2 then "YES" else "NO"  