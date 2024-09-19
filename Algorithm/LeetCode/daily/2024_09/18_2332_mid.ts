/**
 * @Time 2024/09/19 22:53
 * @Author  : https://github.com/hakusai22
 */


function latestTimeCatchTheBus(buses: number[], passengers: number[], capacity: number): number {

    buses.sort((a, b) => a - b)
    passengers.sort((a, b) => a - b)
    let [j, c] = [0, 0]
    for (let t of buses) {
        c = capacity
        while (c && j < passengers.length && passengers[j] <= t) {
            c--
            j++
        }
    }
    --j
    let ans = c > 0 ? buses[buses.length - 1] : passengers[j]
    while (j >= 0 && passengers[j] === ans) {
        j--
        ans--
    }
    return ans
}