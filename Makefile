version := $(shell grep Version SPECS/keycloak.spec | awk '{ print $$2 }')
release := $(shell grep Release SPECS/keycloak.spec | awk '{ print $$2 }' | sed 's|%{?dist}||g')
mock_config := centos-stream+epel-9-x86_64

all: build

srpm:
	rpmbuild -bs --build-in-place SPECS/keycloak.spec

mock: srpm
	mock -r ${mock_config} rebuild SRPMS/keycloak-${version}-${release}.el9.src.rpm

build: srpm mock

