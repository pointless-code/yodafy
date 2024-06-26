import sys

def yoda_transform(text):
    text = text.lower()
    
    words = text.split()
    mid = len(words) // 2
    yoda_speak = words[mid:] + words[:mid]
    return ' '.join(yoda_speak)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print(yoda_transform(input_text))
    else:
        print("Provided to transform, no text")
