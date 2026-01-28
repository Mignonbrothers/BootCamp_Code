# 계산기 만들기

import tkinter

window = tkinter.Tk()
window.title("계산기")
window.geometry("640x400+100+100")
window.resizable(True, True)

entry = tkinter.Entry(window)
entry.grid(row=0, column=0, columnspan=4, sticky="ew")


def click(key):
    if key == '=':
        try:
            result = eval(entry.get())
            entry.delete(0,tkinter.END)
            entry.insert(tkinter.END, str(result))
        except:
            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, "오류")
    elif key == 'C':
        entry.delete(0, tkinter.END)
    else:
        entry.insert(tkinter.END, key)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]


row_num = 1
col_num = 0

for btn_text in buttons:
    # 가장 많이 쓰이는 lambda 방식
    button = tkinter.Button(window, text=btn_text,
                            command=lambda x=btn_text: click(x))

    button.grid(row=row_num, column=col_num, sticky="ew")

    col_num += 1
    if col_num > 3:  # 4열이 다 차면 다음 줄(row)로 이동
        col_num = 0
        row_num += 1
window.mainloop()


# row=0, column=0, columnspan=4, padx=5, pady=5