#Makefile: fotoShoot
#V1 R0
     
# Cleans your directory
clean:
	@ echo "*** Removing all temp files"
	@ rm -f *.pyc
	@ rm -f *~
	@ echo "*** Complete"

# Runs the code
run:
	python2.7 fotoShoot.py

# Build UI for first time !!! USE MAKE BUILD after!!!
initbuild:
	@ echo "***Initial build__Utilizing pyuic4***"
	@ puic4 main.py
	@ echo "Build Success"
	@ echo "!!!!!USE MAKE BUILD for future builds!!!!!!"

# Rebuilds the interface
build:
	@ echo "*** Utilizing pyuic4"
	@ rm main.py
	@ pyuic4 -xd -o main.py main.ui
	@ echo "*** Build Success"
