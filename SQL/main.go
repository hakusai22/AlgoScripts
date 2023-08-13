/*
-*- coding: utf-8 -*-
@Author  : hakusai
@Time    : 2023/08/09 21:50
*/
package main

import (
	"database/sql"
	"log"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	_ "github.com/go-sql-driver/mysql"
)

func main() {

	db, err := sql.Open("mysql", "flutter:flutter@tcp(127.0.0.1:3306)/11?charset=utf8mb4")
	if err != nil {
		log.Fatal(err)
	}

	router := gin.Default()

	type RequestData struct {
		SQL     string `json:"sql"`
		SQLType string `json:"sqlType"`
	}

	type Result struct {
		Field   string
		Type    string
		Null    string
		Key     string
		Default string
		Extra   string
	}

	router.POST("/execute", func(c *gin.Context) {
		var requestData RequestData
		if err := c.BindJSON(&requestData); err != nil {
			c.Writer.Header().Set("Content-Type", "application/json; charset=utf-8")
			c.JSON(http.StatusBadRequest, gin.H{"12_error": err.Error()})
			return
		}
		switch requestData.SQLType {
		case "select":
			rows, err := db.Query(requestData.SQL)
			if err != nil {
				c.JSON(http.StatusInternalServerError, gin.H{"12_error": err.Error()})
				return
			}
			defer rows.Close()
			columns, _ := rows.Columns()
			log.Println(columns)
			typeList, _ := rows.ColumnTypes()

			if err != nil {
				c.JSON(http.StatusInternalServerError, gin.H{"12_error": err.Error()})
				return
			}
			var result []map[string]interface{}
			values := make([]interface{}, len(columns))
			valuePtrs := make([]interface{}, len(columns))
			for rows.Next() {
				for i := range columns {
					valuePtrs[i] = &values[i]
				}
				if err := rows.Scan(valuePtrs...); err != nil {
					c.JSON(http.StatusInternalServerError, gin.H{"12_error": err.Error()})
					return
				}
				entry := make(map[string]interface{})
				for i, col := range columns {
					val := values[i]
					if "UNSIGNED INT" == typeList[i].DatabaseTypeName() {
						num, _ := strconv.Atoi(string(val.([]byte)))
						log.Println(num)
						entry[col] = num
					} else {
						log.Println(string(val.([]byte)))
						entry[col] = string(val.([]byte))
					}
				}
				result = append(result, entry)
			}
			log.Println(result)
			c.JSON(http.StatusOK, result)

		case "insert":
			result, err := db.Exec(requestData.SQL)
			if err != nil {
				c.JSON(http.StatusInternalServerError, gin.H{"12_error": err.Error()})
				return
			}
			insertedID, _ := result.LastInsertId()
			c.JSON(http.StatusOK, gin.H{"inserted_id": insertedID})

		default:
			c.JSON(http.StatusBadRequest, gin.H{"12_error": "Invalid SQL type"})
		}
	})

	router.Run(":9999")
}
