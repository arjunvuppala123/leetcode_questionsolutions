public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
            return false;

        int n = s.Length;
        int[] charArray = new int[26];

        for (int i = 0; i < n; i++){
            charArray[s[i] - 'a']++;
            charArray[t[i] - 'a']--;
        }

        for (int i = 0; i < 26; i++){
            if (charArray[i] != 0)
                return false;
        }

        return true;
    }
}

/* public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> hashMap1 = new();
        Dictionary<char, int> hashMap2 = new();

        if (s.Length != t.Length)
            return false;

        for (int i = 0; i < s.Length; i++){
            if (hashMap1.ContainsKey(s[i]))
                hashMap1[s[i]]++;
            else
                hashMap1.Add(s[i], 1);

            if (hashMap2.ContainsKey(t[i]))
                hashMap2[t[i]]++;
            else
                hashMap2.Add(t[i], 1);
        }

        foreach (var key in hashMap1){
            if (!hashMap2.TryGetValue(key.Key, out int value2) || key.Value != value2)
            return false;
        }

        return true;
    }
}*/
