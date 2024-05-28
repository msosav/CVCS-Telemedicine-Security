#include "LZW.h"
#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

LZW::LZW() {
    initialize_dictionary();
}

void LZW::initialize_dictionary() {
    dictionary.clear();
    for (int i = 0; i < 256; ++i) {
        string ch(1, static_cast<char>(i));
        dictionary[ch] = i;
    }
}

vector<vector<LZW::Pixel>> LZW::read_BMP(const char *nombreArchivo, struct BMPHeader &header)
{
    ifstream archivo(nombreArchivo, ios::binary);
    if (!archivo)
    {
        throw runtime_error("No se pudo abrir el archivo");
    }
    archivo.read(reinterpret_cast<char *>(&header), sizeof(BMPHeader));
    archivo.seekg(header.dataOffSet, ios::beg);
    vector<vector<LZW::Pixel>> matriz(header.height, vector<LZW::Pixel>(header.width));
    for (int i = 0; i < header.height; i++)
    {
        for (int j = 0; j < header.width; j++)
        {
            archivo.read(reinterpret_cast<char *>(&matriz[i][j]), sizeof(LZW::Pixel));
        }
        archivo.seekg(header.width % 4, ios::cur);
    }
    archivo.close();
    return matriz;
}

void LZW::write_BMP(const char *nombreArchivo, const struct BMPHeader &header, const vector<vector<LZW::Pixel>> &matriz)
{
    ofstream archivo(nombreArchivo, ios::binary);
    if (!archivo)
    {
        throw runtime_error("No se pudo abrir el archivo");
    }
    archivo.write(reinterpret_cast<const char *>(&header), sizeof(BMPHeader));
    archivo.seekp(header.dataOffSet, ios::beg);
    for (int i = 0; i < header.height; i++)
    {
        for (int j = 0; j < header.width; j++)
        {
            archivo.write(reinterpret_cast<const char *>(&matriz[i][j]), sizeof(LZW::Pixel));
        }
        archivo.seekp(header.width % 4, ios::cur);
    }
    archivo.close();
}

void LZW::compress(vector<vector<LZW::Pixel>>& input_image_matrix, const string& output_file) {
    ofstream fout(output_file, ios::binary);

    if (!fout) {
        cerr << "Error opening output file." << endl;
        return;
    }

    int width = input_image_matrix[0].size();
    int height = input_image_matrix.size();
    fout.write(reinterpret_cast<const char*>(&width), sizeof(width));
    fout.write(reinterpret_cast<const char*>(&height), sizeof(height));

    string previous, entry;
    for (const auto& row : input_image_matrix) {
        for (const auto& pixel : row) {
            string current(1, pixel.red);
            entry = previous + current;
            if (dictionary.find(entry) != dictionary.end()) {
                previous = entry;
            } else {
                write_code(dictionary[previous], fout);
                dictionary[entry] = dictionary.size();
                previous = current;
            }
        }
    }

    if (!previous.empty()) {
        write_code(dictionary[previous], fout);
    }

    fout.close();
}

void LZW::compress(const string& input_image, const string& output_file) {
    LZW::BMPHeader header;
    vector<vector<LZW::Pixel>> input_image_matrix = read_BMP(input_image.c_str(), header);
    compress(input_image_matrix, output_file);
}

void LZW::write_code(int code, ofstream& fout) {
    fout.write(reinterpret_cast<const char*>(&code), sizeof(code));
}