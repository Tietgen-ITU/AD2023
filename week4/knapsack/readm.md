Vi skal til at lave nogle cases der kan udmønte sig i nogle base cases:

# Case 1
$sack_{cap}=5$ 

Input:
[(1, 5),(5, 5), (10, 5)]

# Case 2
$sack_{cap}=6$ 

Input:
[(1, 6),(5, 5), (2, 1), (2, 1)]

Run:

                            Solve(6)
            solve(5)                        solve(4)
    solve(4)        solve(3)           solve(3)   solve(2)
solve(2)  solve(1)  ......

Cases:

solve(n) = max(solve(n-1), solve(n-2))