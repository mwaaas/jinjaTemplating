deploy:
	docker build -t mwaaas/jinja_evaluation .
	docker push mwaaas/jinja_evaluation