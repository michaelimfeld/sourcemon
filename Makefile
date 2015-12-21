all: # nothing to build

install:
	mkdir -p $(DESTDIR)/usr/share/sourcemon
	cp -r bin/* $(DESTDIR)/usr/share/sourcemon
	mkdir -p $(DESTDIR)/var/www/sourcemon
	cp -r sourcemon/* $(DESTDIR)/var/www/sourcemon
