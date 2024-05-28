#ifndef LZW_H
#define LZW_H

#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

class LZW
{
public:
    LZW();

    struct Pixel
    {
        unsigned char red, green, blue;
    };

    #pragma pack(push, 1)
    struct BMPHeader {
        char signature[2];
        int fileSize;
        int reserved;
        int dataOffSet;
        int headerSize;
        int width;
        int height;
        short planes;
        short bitsPerPixel;
        int compression;
        int dataSize;
        int horizontalResolution;
        int verticalResolution;
        int colors;
        int importantColors;
    };

    #pragma pack(pop)
    vector<vector<LZW::Pixel>> read_BMP(const char *nombreArchivo, struct BMPHeader &header);
    void write_BMP(const char *nombreArchivo, const struct BMPHeader &header, const vector<vector<LZW::Pixel>> &matriz);

    void compress(vector<vector<Pixel>>& input_image_matrix, const string& output_file);
    void compress(const string& input_image, const string& output_file);

    void decompress(const string& input_file, vector<vector<Pixel>>& output_image_matrix);

private:

    void initialize_dictionary();
    void write_code(int code, ofstream &fout);
    int read_code(ifstream &fin);

    unordered_map<string, int> dictionary;
};

#endif // LZW_H
