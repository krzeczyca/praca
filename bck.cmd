rem ale jazda
FOR /F "tokens=1-3 delims= " %%A IN ('dir "C:\tmp\log\*.log" /b /o-d') DO (
  IF %count% LEQ 2 (
    set "file=%%A %%B %%C"
    set /a count+=1
	set count
  ) ELSE  (
    set "file=%%A %%B %%C"
	move "C:\tmp\log\%file%" "C:\tmp\log2"
  )
)
set count=0
