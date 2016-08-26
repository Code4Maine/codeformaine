install:
	virtualenv -p python3 venv
	venv/bin/python setup.py install
	venv/bin/python manage.py migrate --noinput


deps_js:
	npm install
	./node_modules/.bin/gulp sass

deps:
	sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk libxslt-dev libxml2-dev
	npm install
	

deps_mac:
	brew install libtiff libjpeg webp little-cms2
	npm install


test:
	rm -rf .tox
	detox

clean:
	rm -rf venv
	rm -rf dist
	rm -rf .deploy

run:
	venv/bin/python manage.py runserver_plus 0.0.0.0:45000

rename:
	find . -maxdepth 1 -type f \( ! -iname "Makefile" \) -print0 | xargs -0 sed -i 's/codeformaine/$(name)/g'
	find codeformaine -maxdepth 1 -type f -print0 | xargs -0 sed -i 's/codeformaine/$(name)/g'
	mv codeformaine/manage_codeformaine.py codeformaine/manage_$(name).py
	mv codeformaine $(name)
	echo "Great, you're all set! Well, you'll probably want to adjust the setup file by hand a bit."

tag-release:
	sed -i "/__version__/c\__version__ = '$(v)'" codeformaine/__init__.py
	git add codeformaine/__init__.py && git commit -m "Automated version bump to $(v)" && git push
	git tag -a release/$(v) -m "Automated release of $(v) via Makefile" && git push origin --tags

package:
	rm -rf build
	python setup.py clean
	python setup.py sdist bdist_wheel

distribute:
	twine upload -s dist/codeformaine-$(v)*

release:
	$(MAKE) tag-release
	$(MAKE) package
	$(MAKE) distribute

launch_deps:
	mkdir .deploy
	virtualenv -p python2 .deploy/venv
	.deploy/venv/bin/pip install ansible

stage:
	$(MAKE) launch_deps
	.deploy/venv/bin/ansible-playbook -i ansible/hosts --limit cfm --tags deploy --extra-vars '{"app_version":"$(v)"}' ansible/launch.yml -u cfm_production

deploy:
	$(MAKE) launch_deps
	.deploy/venv/bin/ansible-playbook -i ansible/hosts --limit cfm --tags deploy .deploy/ansible/launch.yml -u cfm_production


redeploy:
	$(MAKE) launch_deps
	.deploy/venv/bin/ansible-playbook -i ansible/hosts --limit cfm --tags deploy --extra-vars '{"app_version":"$(v)"}' ansible/launch.yml -u cfm_production

reconfigure:
	$(MAKE) launch_deps
	.deploy/venv/bin/ansible-playbook -i ansible/hosts --limit $(h) --tags reconfigure ansible/launch.yml -u cfm_production

