file = open('/Users/rmittal/programs/clusters/radio_lum/correlation-plots/HIFLUGCS_XR_correlation_badformat.txt')
data = []
colwidths = []
for line in file:
   data.append(line.split())
   for i, d in enumerate(data[-1]):
       if len(colwidths) <= i:
          colwidths.append(len(d))
       elif len(d) > colwidths[i]:
          colwidths[i] = len(d)
file.close()

fmtstr = '    '.join(['%'+str(n)+'s' for n in colwidths])

for row in data:
   print fmtstr % tuple(row)
