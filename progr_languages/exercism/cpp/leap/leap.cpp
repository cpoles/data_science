#include "leap.h"

namespace leap {

    bool is_leap_year(int x) {
    
            if((x % 4 == 0 && x % 100 != 0) || x % 400 == 0) {
    
                return true;
    
            }
    
            return false;
    
        }

}  // namespace leap
