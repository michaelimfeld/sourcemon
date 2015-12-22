all: # nothing to build

install:
	# copy python files
	mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages/sourcemon/model
	cp sourcemon/*.py $(DESTDIR)/usr/lib/python2.7/dist-packages/sourcemon
	cp sourcemon/model/*.py $(DESTDIR)/usr/lib/python2.7/dist-packages/sourcemon/model
	# copy bin
	mkdir -p $(DESTDIR)/usr/bin
	cp sourcemon/main.py $(DESTDIR)/usr/bin/sourcemon
	# copy setup_db script
	mkdir -p $(DESTDIR)/usr/share/sourcemon
	cp -r bin/* $(DESTDIR)/usr/share/sourcemon
	# copy static files
	mkdir -p $(DESTDIR)/var/www/sourcemon
	cp -r sourcemon/static $(DESTDIR)/var/www/sourcemon
	cp -r sourcemon/templates $(DESTDIR)/var/www/sourcemon

