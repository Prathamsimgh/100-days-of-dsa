def is_palindrome(s: str) -> bool:
    """True if s is a palindrome after dropping non-alphanumerics and
    case-folding.

    Two pointers converge from both ends, skipping anything that is not
    alphanumeric. O(n) time, O(1) extra space.
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("") is True
    assert is_palindrome("ab") is False
    assert is_palindrome("aa") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("Madam") is True
    assert is_palindrome(".,") is True
    assert is_palindrome("ab_a") is True
    print("all tests passed")
