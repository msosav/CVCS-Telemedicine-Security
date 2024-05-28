#include "Compressing/LZW.h"
#include <iostream>

using namespace std;

int main() {
    try {
        // Path to the input image
        string inputImagePath = "input_image.bmp";
        // Path to the output compressed file
        string outputCompressedPath = "compressed.lzw";

        // Compress the image
        LZW lzw;
        lzw.compress(inputImagePath, outputCompressedPath);

        cout << "Compression and decompression completed successfully!" << endl;
    } catch (const exception& e) {
        cerr << "An error occurred: " << e.what() << endl;
    }

    return 0;
}
