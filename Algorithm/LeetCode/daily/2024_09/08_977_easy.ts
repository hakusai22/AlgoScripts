/**
 * @Time 2024/09/08 10:02
 * @Author  : https://github.com/hakusai22
 */

function sortedSquares(nums: number[]): number[] {
    let start: number = 0
    let end: number = nums.length - 1
    let store_index = end
    let num: number[] = [];
    while (start <= end) {
        let start_number = Math.pow(nums[start], 2);
        let end_number = Math.pow(nums[end], 2);
        //根据数学平方原理 越是靠近0的平方越是小 只用比较两端就好了 比较好的数直接放后端
        if (start_number > end_number) {
            num[store_index--] = start_number;
            start++;
        } else {
            num[store_index--] = end_number;
            end--;

        }

    }
    return num;
}

console.log(sortedSquares([-4,-1,0,3,10]))