#ifndef _CPPMAIN_
#define _CPPMAIN_

class Board{
    public:
        int get_rows();
        int get_cols();
    private:
        static const int ROWS = 6;
        static const int COLS = 7; 
};

int Board::get_rows(void) {
    return ROWS;
}
int Board::get_cols(void) {
    return COLS;
}

#endif //_CPPMAIN_