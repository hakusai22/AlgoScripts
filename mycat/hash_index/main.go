package main

import (
	"Go_Study/mycat/hash"
	"fmt"
	"sort"
)

func tailMap(m map[uint32]int, key uint32) map[uint32]int {
	keys := make([]uint32, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	sort.Slice(keys, func(i, j int) bool {
		return keys[i] < keys[j]
	})

	index := 0
	for _, k := range keys {
		if key <= k {
			break
		}
		index++
	}
	keys = keys[index:]
	result := make(map[uint32]int)
	for _, k := range keys {
		result[k] = m[k]
	}
	return result
}

func generHash(count, virtualBucketTimes int) map[uint32]int {
	bucketMap := make(map[uint32]int)
	for i := 0; i < count; i++ {
		shard := virtualBucketTimes * 1
		for n := 0; n < shard; n++ {
			prefix := fmt.Sprintf("SHARD-%d-NODE-%d", i, n)
			hashCode := hash.HashUnencodedChars(0, prefix)
			bucketMap[uint32(hashCode)] = i
		}
	}
	return bucketMap
}

func getMurmurHashIndex(count, virtualBucketTimes int, userID string) int {
	bucketMap := generHash(count, virtualBucketTimes)
	hashCode := hash.HashUnencodedChars(0, userID)
	s := tailMap(bucketMap, uint32(hashCode))
	if len(s) > 0 {
		var keys []uint32
		for k := range s {
			keys = append(keys, k)
		}
		sort.Slice(keys, func(i, j int) bool {
			return keys[i] < keys[j]
		})
		return s[keys[0]]
	}
	var keys []uint32
	for k := range bucketMap {
		keys = append(keys, k)
	}
	sort.Slice(keys, func(i, j int) bool {
		return keys[i] < keys[j]
	})
	return bucketMap[keys[0]]
}

func main() {
	userID := "1231231"
	fmt.Println(getMurmurHashIndex(128, 4, userID))
}
