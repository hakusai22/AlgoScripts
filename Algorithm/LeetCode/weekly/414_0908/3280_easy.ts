/**
 * @Time 2024/09/08 15:32
 * @Author  : https://github.com/hakusai22
 */

function convertDateToBinary(date: string): string {
    return date.split('-').map(time => (+time).toString(2)).join('-');
}

console.log(convertDateToBinary("2080-02-29"))