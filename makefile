#Makefile: fotoShoot
#V1 R1
     
# Cleans your directory
clean:
	@ echo "*** Removing all temp files ***"
	@ rm -f *.pyc
	@ rm -f *~
	@ echo "*** Complete ***"

# Runs the code
run:
	python2.7 fotoShoot.py

# Build UI for first time !!! USE MAKE BUILD after!!!
initbuild:
	#Build main UI
	@ echo "***Initial build__Utilizing pyuic4***"
	@ pyuic4 main.py
	
	#Build slide show UI
	@ pyuic4 frame.py
	@ echo "Build Success"
	@ echo "!!!!!USE MAKE BUILD for future builds!!!!!!"

# Rebuilds the interface
build:
	#Build main UI
	@ echo "*** Utilizing pyuic4 ***"
	@ rm main.py
	@ pyuic4 -xd -o main.py main.ui
	
	#Build slide show UI
	@ rm frame.py
	@ pyuic4 -xd -o frame.py frame.ui
	@ echo "*** Build Success ***"
