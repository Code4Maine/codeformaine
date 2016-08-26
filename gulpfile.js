'use strict';
 
var gulp = require('gulp');
var sass = require('gulp-sass');
var rename = require('gulp-rename');
var minifyCSS = require('gulp-minify-css');
 
gulp.task('sass', function () {
  return gulp.src('codeformaine/static/scss/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(minifyCSS({processImport: false}))
    .pipe(rename('app.css'))
    .pipe(gulp.dest('codeformaine/static/css'));
});
 
gulp.task('sass:watch', function () {
  gulp.watch('codeformaine/static/scss/**/*.scss', ['sass']);
});

gulp.task('default', ['sass:watch']);
