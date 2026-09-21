n=int(input("Enter number of elements:"));
st=[];
for i in range(n):
    x=int(input("Enter element:"))
    st.append(x)
st.reverse()
print("stack of element:",st)    