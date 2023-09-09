package hash

import (
	"sort"
	"strconv"
)

func int_overflow(val int64) int {
	maxint := 2147483647
	maxint32 := int64(maxint)
	if val < -maxint32-1 {
		res := ((val+(maxint32+1))%(2*(maxint32+1))+(2*(maxint32+1)))%(2*(maxint32+1)) - maxint32 - 1
		return int(res)
	}
	if val > maxint32 {
		res := (val+(maxint32+1))%(2*(maxint32+1)) - maxint32 - 1
		return int(res)
	} else {
		return int(val)
	}
}

func unsigned_right_shift(n, i int) int {
	if n < 0 {
		a := uint32(n)
		n = int(a)
	}
	if i < 0 {
		return -int_overflow(int64(n << -i))
	}
	return int_overflow(int64(n >> i))
}

func rotateLeft(i, distance int) int {
	return int_overflow(int64(i<<distance)) | unsigned_right_shift(i, 32-distance)
}

func mixK1(k1 int) int {
	k1 = int_overflow(int64(k1 * -862048943))
	k1 = int_overflow(int64(rotateLeft(k1, 15)))
	k1 = int_overflow(int64(k1 * 461845907))
	//fmt.Println(k1)
	return k1
}

func mixH1(h1, k1 int) int {
	h1 ^= k1
	h1 = rotateLeft(h1, 13)
	h1 = int_overflow(int64(h1*5 + -430675100))
	return h1
}

func fmix(h1, length int) int {
	h1 ^= length
	h1 ^= unsigned_right_shift(h1, 16)
	h1 = int_overflow(int64(h1 * -2048144789))
	h1 ^= unsigned_right_shift(h1, 13)
	h1 = int_overflow(int64(h1 * -1028477387))
	h1 ^= unsigned_right_shift(h1, 16)
	return h1
}

func HashUnencodedChars(seed int, input string) int {
	//fmt.Println(seed)
	//fmt.Println(input)
	h1 := seed
	for k1 := 1; k1 < len(input); k1 += 2 {
		//fmt.Println(string(input[k1-1]))
		t := int(input[k1-1])
		//fmt.Println(t)
		gg := t | int(input[k1])<<16
		//fmt.Println(gg)
		gg2 := mixK1(gg)
		//fmt.Println(gg2)
		h1 = mixH1(h1, gg2)
		//fmt.Println(h1)
	}
	//fmt.Println(h1)
	if (len(input) & 1) == 1 {
		k1 := int(input[len(input)-1])
		k1 = mixK1(k1)
		h1 ^= k1
	}
	return fmix(h1, 2*len(input))
}

// ---------------

func tail_map(m map[int]int, key int) map[int]int {
	keys := make([]int, 0, len(m))
	m_2 := map[int]int{}
	for k, _ := range m {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	idx := sort.Search(len(keys), func(i int) bool {
		return keys[i] >= key
	})

	for i, k := range keys {
		if i >= idx {
			m_2[k] = m[k]
		}
	}
	return m_2
}

func gener_hash(count, virtualBucketTimes int) map[int]int {
	bucketMap := map[int]int{}
	for i := 0; i < count; i++ {
		shard := virtualBucketTimes * 1
		for n := 0; n < shard; n++ {
			prefix := "SHARD-" + strconv.Itoa(i) + "-NODE-"
			bucketMap[HashUnencodedChars(0, prefix+strconv.Itoa(n))] = i
		}
	}
	return bucketMap
}

func Get_murmur_hash_index(count, virtualBucketTimes, user_id int) string {
	userid := strconv.Itoa(user_id)
	bucketMap := gener_hash(count, virtualBucketTimes)
	// print(sorted(bucketMap))
	//fmt.Println(bucketMap)
	hash_code := HashUnencodedChars(0, userid)
	// print(testHash.hashUnencodedChars(0, '0'))
	s := tail_map(bucketMap, hash_code)
	if len(s) > 0 {
		var _min int
		for k, _ := range s {
			_min = k
			break
		}
		for k, _ := range s {
			if k < _min {
				_min = k
			}
		}
		return strconv.Itoa(s[_min])

	} else {
		var _min int
		for k, _ := range bucketMap {
			_min = k
			break
		}
		for k, _ := range bucketMap {
			if k < _min {
				_min = k
			}
		}
		return strconv.Itoa(bucketMap[_min])
	} //# print(keys)
}
