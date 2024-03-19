# Print the following pattern

def numbered_pyramide(n):
    for i in range (1,n+1):
        line = ''
        for j in range (0, i):
            string_i = str(i)
            line += ' ' + string_i
        print (line)

numbered_pyramide(5)

# def numbered_pyramide(n):
#     for i in range (1,n+1):
#         line = []
#         for j in range (0, i):
#             line.append(i)
#         print (line)