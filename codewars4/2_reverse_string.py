def reverse(st):
    list_st = st.split()
    list_st.reverse()
    st = ' '.join(list_st)
    return st


print(reverse('Hello World'))
print(reverse('Hi There.'))
