/**
 * @Time 2024/10/08 00:10
 * @Author  : https://github.com/hakusai22
 * @题目     :
 * @参考     :
 * @时间复杂度:
 * @空间复杂度:
 */

const XLSX = require('xlsx');
const fs = require('fs');

// 读取 Excel 文件
function readExcel(filePath) {
    const workbook = XLSX.readFile(filePath);
    const sheetName = workbook.SheetNames[0]; // 读取第一个工作表
    const sheet = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName]);
    return sheet;
}

// 查找对应的parameter值
function findParameter(data, 数据来源, type) {
    const result = data.find(item => item['数据来源'] === 数据来源 && item['type'] === type);
    return result ? result['parameter'] : '未找到对应的parameter';
}

// 示例
const filePath = './search_parameter.xlsx'; // Excel 文件的路径
const data = readExcel(filePath);

// 指定查找的数据来源和type
const 数据来源 = 'LL';
const type = 'C';

// 查找并输出结果
const parameterValue = findParameter(data, 数据来源, type);
console.log(`Parameter值: ${parameterValue}`);
