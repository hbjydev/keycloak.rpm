version := $(shell grep Version SPECS/keycloak.spec | awk '{ print $$2 }')
release := $(shell grep Release SPECS/keycloak.spec | awk '{ print $$2 }' | sed 's|%{?dist}||g')
mock_config := centos-stream+epel-9-x86_64
mock_dir := /var/lib/mock/${mock_config}
srpm_name := keycloak-${version}-${release}.el9.src.rpm

all: build

link:
	ln -sf $(shell pwd) ${HOME}/rpmbuild

deps:
	spectool -g -C SOURCES SPECS/keycloak.spec

srpm: deps
	mock -r ${mock_config} --buildsrpm --spec SPECS/keycloak.spec --sources SOURCES
	cp ${mock_dir}/result/${srpm_name} /tmp/${srpm_name}

mock: srpm
	mock -r ${mock_config} --rebuild /tmp/${srpm_name}

build: mock

