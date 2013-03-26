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

# Rebuilds the interface
build:
	@ echo "*** Utilizing pyuic4"
	@ pyuic4 -xd -o fotoShootWidget.py main.ui
	@ echo "*** Build Success"
