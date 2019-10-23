package main
func lengthOfLongestSubstring(s string) int {
    charIndex := make(map[rune]int)
    start, maxLength, length := 0, 0, 0
    for i, v := range []rune(s) {
        if lastIndex, ok := charIndex[v]; ok && lastIndex >= start {
            start = lastIndex + 1
            length = i - start + 1
        } else {
            length += 1
        }
        charIndex[v] = i
        if length > maxLength {
            maxLength = length
        }
    }
    return maxLength
}
