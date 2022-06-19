version := $(shell grep Version SPECS/keycloak.spec | awk '{ print $$2 }')
release := $(shell grep Release SPECS/keycloak.spec | awk '{ print $$2 }' | sed 's|%{?dist}||g')
mock_config := centos-stream+epel-9-x86_64

all: build

link:
	ln -sf $(shell pwd) ${HOME}/rpmbuild

deps:
	spectool -g -C SOURCES SPECS/keycloak.spec

srpm: deps
	rpmbuild -bs --root $(shell pwd) SPECS/keycloak.spec

mock: srpm
	mock -r ${mock_config} rebuild SRPMS/keycloak-${version}-${release}.el9.src.rpm

build: mock

