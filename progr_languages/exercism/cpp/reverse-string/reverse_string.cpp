#include "reverse_string.h"

namespace reverse_string {

    std::string reverse_string(std::string str) {
        if (str.empty())
            return "";
        
        std::string rev_str;
        for (size_t i = str.length(); i > 0; i--)
        {
            size_t j = str.length() - i;
            rev_str[j] = str[i];
        }
        return rev_str;
        
    }

}  // namespace reverse_string
