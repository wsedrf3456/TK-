#!/usr/bin/python3
# 스크립트를 해석하기 위해 시작해야 하는 프로그램 파악
# .! which python3 로 파이썬3의 위치 파악과 동시에 커서에 복붙 가능

# http://www.tkdocs.com/tutorial/firstexample.html
# 참고한 홈페이지를 주석으로 명시

from tkinter import *
# tkinter 모듈로부터 모든 함수를 불러옴
# 모듈이란?
# 1. 함수나 변수 또는 클래스 들을 모아 놓은 것
# 2. 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만들어진 파이썬 파일

from tkinter import ttk
# tkinter에서 새로 추가된 ttk 불러옴

def calculate(*args):
# calculate 함수 만들기

	try:	
	# 오류처리
		value = float(feet.get())
		meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
	except ValueError:
		pass

root=Tk()
# tk()를 통해 기본창 띄우기!
root.title("Feet to Meters")
# 제목 설정
	
mainframe = ttk.Frame(root, padding="3 3 12 12")
# 동,서,남,북 길이 결정
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# mainframe 을 격자무늬 기준 0행 0열 좌우상하 대칭으로 지정
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
# mainframe 열과 행 넓이 1로 환경설정!

feet = StringVar()
#
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# mainframe에 넓이가 7인 빈칸 만들기
feet_entry.grid(column=2, row=1, sticky = (W, E))
# 1행 2열 좌우대칭으로 빈칸 위치설정

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=E)
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
# 프로그램 실행 시 마우스커서가 자동으로 빈칸에 가있게 설정
root.bind('<Return>', calculate)
# Return : 엔터키 / 엔터키로 calculate 가능

root.mainloop()
# GUI 는 순서대로 실행하지 않기때문에 빠르게 프로그램을 처음부터 끝까지 지속적으로 돌려주는 역할
