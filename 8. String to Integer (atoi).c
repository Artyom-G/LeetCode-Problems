//Time Complexity: O(n)
//Space Complexity: O(1)
int myAtoi(char *s) {
    long result = 0; // Use long to handle overflow
    int sign = 1;
    int index = 0;

    // Skip leading whitespaces
    while (s[index] == ' ') {
        index++;
    }

    // Handle sign
    if (s[index] == '-' || s[index] == '+') {
        sign = (s[index] == '-') ? -1 : 1;
        index++;
    }

    // Read digits and convert to int
    while (s[index] >= '0' && s[index] <= '9') {
        result = result * 10 + (s[index] - '0');
        index++;

        // Handle overflow and underflow
        if (sign == 1 && result > INT_MAX) {
            return INT_MAX;
        } else if (sign == -1 && -result < INT_MIN) {
            return INT_MIN;
        }
    }

    // Apply the sign
    result *= sign;

    // Clamp the result to INT boundaries
    if (result > INT_MAX) {
        return INT_MAX;
    } else if (result < INT_MIN) {
        return INT_MIN;
    }

    return (int)result;
}
