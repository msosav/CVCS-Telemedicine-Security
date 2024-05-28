# Compiler to use
CXX = g++

# Flags to pass to compiler
CXXFLAGS = -Wall -g

# Name of the output file
OUTPUT = cvcs

# Source files
SRCS = main.cpp Compressing/LZW.cpp

# Header files
HDRS = Compressing/LZW.h

all: $(OUTPUT)

$(OUTPUT): $(SRCS)
	$(CXX) $(CXXFLAGS) -o $(OUTPUT) $(SRCS)

clean:
	rm -f $(OUTPUT)
