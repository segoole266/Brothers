[app]

# (str) Title of your application
title = Brothers 4.0

# (str) Package name
package.name = brothers

# (str) Package domain (needed for android/ios packaging)
package.domain = org.brothers

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ico,ttf

# (list) List of inclusions using pattern matching
source.include_patterns = *.png,*.ico,*.ttf

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, docs, __pycache__, .git

# (list) List of exclusions using pattern matching
# source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 4.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = python3,kivy,yt-dlp

# (str) Custom source folders for requirements
# requirements.pip = yt-dlp

# (list) Garden requirements
# garden_requirements =

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = Brothers.ico

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 2.1.0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
# android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 33

# (str) Android NDK version to use
android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Android Java class name
# android.main_class = org.kivy.android.PythonActivity

# (str) python-for-android git branch to use, if not master
# p4a.branch = master

# (str) OUYA Console category. Should be one of GAME or APP
# ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
# ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
# android.manifest.intent_filters =

# (list) Android additionnal libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/android/*.so
# android.add_libs_armeabi_v7a = libs/android-v7/*.so
# android.add_libs_arm64_v8a = libs/android-v8/*.so
# android.add_libs_x86 = libs/android-x86/*.so
# android.add_libs_x86_64 = libs/android-x86_64/*.so

# (bool) Indicate whether the screen should stay on
# android.wakelock = False

# (list) Android application meta-data to set
# android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
# android.library_references =

# (list) Android shared libraries which will be loaded by the system before
# loading the app
# android.shared_libraries =

# (list) Android AAR archives to add (will be added in the
# project.properties automatically.)
# android.aar_references =

# (list) Gradle dependencies to add (will be added in the
# build.gradle automatically.)
# android.gradle_dependencies =

# (list) Java classes to add as activities to the manifest.
# android.add_activity =

# (str) python-for-android branch to use, if not stable
# p4a.branch = stable

# (str) OUYA Console category. Should be one of GAME or APP
# ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
# ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
# android.manifest.intent_filters =

# (list) Android additionnal libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/android/*.so
# android.add_libs_armeabi_v7a = libs/android-v7/*.so
# android.add_libs_arm64_v8a = libs/android-v8/*.so
# android.add_libs_x86 = libs/android-x86/*.so
# android.add_libs_x86_64 = libs/android-x86_64/*.so

# (bool) Indicate whether the screen should stay on
# android.wakelock = False

# (list) Android application meta-data to set
# android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
# android.library_references =

# (list) Android shared libraries which will be loaded by the system before
# loading the app
# android.shared_libraries =

# (list) Android AAR archives to add (will be added in the
# project.properties automatically.)
# android.aar_references =

# (list) Gradle dependencies to add (will be added in the
# build.gradle automatically.)
# android.gradle_dependencies =

# (list) Java classes to add as activities to the manifest.
# android.add_activity =

# (str) python-for-android branch to use, if not stable
# p4a.branch = stable

# (str) OUYA Console category. Should be one of GAME or APP
# ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
# ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
# android.manifest.intent_filters =

# (list) Android additionnal libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/android/*.so
# android.add_libs_armeabi_v7a = libs/android-v7/*.so
# android.add_libs_arm64_v8a = libs/android-v8/*.so
# android.add_libs_x86 = libs/android-x86/*.so
# android.add_libs_x86_64 = libs/android-x86_64/*.so

# (bool) Indicate whether the screen should stay on
# android.wakelock = False

# (list) Android application meta-data to set
# android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
# android.library_references =

# (list) Android shared libraries which will be loaded by the system before
# loading the app
# android.shared_libraries =

# (list) Android AAR archives to add (will be added in the
# project.properties automatically.)
# android.aar_references =

# (list) Gradle dependencies to add (will be added in the
# build.gradle automatically.)
# android.gradle_dependencies =

# (list) Java classes to add as activities to the manifest.
# android.add_activity =

# (str) python-for-android branch to use, if not stable
# p4a.branch = stable

# (str) OUYA Console category. Should be one of GAME or APP
# ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
# ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
# android.manifest.intent_filters =

# (list) Android additionnal libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/android/*.so
# android.add_libs_armeabi_v7a = libs/android-v7/*.so
# android.add_libs_arm64_v8a = libs/android-v8/*.so
# android.add_libs_x86 = libs/android-x86/*.so
# android.add_libs_x86_64 = libs/android-x86_64/*.so

# (bool) Indicate whether the screen should stay on
# android.wakelock = False

# (list) Android application meta-data to set
# android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
# android.library_references =

# (list) Android shared libraries which will be loaded by the system before
# loading the app
# android.shared_libraries =

# (list) Android AAR archives to add (will be added in the
# project.properties automatically.)
# android.aar_references =

# (list) Gradle dependencies to add (will be added in the
# build.gradle automatically.)
# android.gradle_dependencies =

# (list) Java classes to add as activities to the manifest.
# android.add_activity =

# (str) python-for-android branch to use, if not stable
# p4a.branch = stable

#
# iOS specific
#

# (str) iOS bundle identifier
# ios.bundle_identifier = org.brothers.brothers

# (list) iOS requirements to add
# ios.requirements = kivy

# (str) iOS framework to add
# ios.frameworks = libs/ios/libzbar.a

# (str) iOS extra frameworks to add
# ios.extra_frameworks = libs/ios/libzbar.a

# (str) iOS minimum version
# ios.min_version = 9.0

# (str) iOS SDK version
# ios.sdk_version = 13.0

# (str) iOS deployment target
# ios.deployment_target = 9.0

# (str) iOS icons
# ios.icons = %(source.dir)s/data/icon.png

# (str) iOS plist
# ios.plist = %(source.dir)s/data/Info.plist

# (str) iOS bundle name
# ios.bundle_name = Brothers 4.0

# (list) iOS additionnal frameworks
# ios.frameworks =

# (list) iOS additionnal libraries
# ios.libraries =

# (list) iOS additionnal pkg
# ios.pkg =

# (str) iOS presplash
# ios.presplash =

# (str) iOS storyboard
# ios.storyboard =

# (list) iOS plist entries
# ios.plist_entries =

# (str) iOS app icon
# ios.app_icon = %(source.dir)s/data/icon.png

# (str) iOS launch image
# ios.launch_image = %(source.dir)s/data/launch.png

#
# Windows specific
#

# (list) Windows requirements
# windows.requirements = kivy

# (list) Windows png files
# windows.icon = %(source.dir)s/data/icon.png

# (list) Windows exe output
# windows.exe = Brothers.exe

# (list) Windows splash screen
# windows.splash = %(source.dir)s/data/splash.png

# (list) Windows application data
# windows.app_data = %(source.dir)s/data/app_data

#
# Web specific
#

# (bool) web debugging
# web.debug = False

# (str) web framework
# web.framework = pyjnius

# (str) web app name
# web.app_name = Brothers 4.0

# (str) web app main file
# web.main = index.html

# (str) web app icon
# web.icon = %(source.dir)s/data/icon.png

# (str) web app presplash
# web.presplash = %(source.dir)s/data/presplash.png

# (str) web app manifest
# web.manifest = %(source.dir)s/data/manifest.json

# (list) web app service worker
# web.service_worker =

# (list) web app extra files
# web.extra_files =

#
# Linux specific
#

# (str) Linux desktop file
# linux.desktop = %(source.dir)s/data/brothers.desktop

# (str) Linux app icon
# linux.icon = %(source.dir)s/data/icon.png

# (str) Linux app name
# linux.app_name = Brothers 4.0

# (str) Linux app version
# linux.app_version = 4.0.0

# (str) Linux app author
# linux.app_author = Brothers

# (str) Linux app comment
# linux.app_comment = YouTube Downloader

# (str) Linux app categories
# linux.app_categories = Network;AudioVideo;

# (str) Linux app keywords
# linux.app_keywords = downloader;youtube;video;audio;

# (str) Linux app startup notify
# linux.app_startup_notify = false

# (str) Linux app terminal
# linux.app_terminal = false

# (str) Linux app type
# linux.app_type = Application

# (str) Linux app icon
# linux.icon = %(source.dir)s/data/icon.png

# (str) Linux desktop file
# linux.desktop = %(source.dir)s/data/brothers.desktop

# (str) Linux app name
# linux.app_name = Brothers 4.0

# (str) Linux app version
# linux.app_version = 4.0.0

# (str) Linux app author
# linux.app_author = Brothers

# (str) Linux app comment
# linux.app_comment = YouTube Downloader

# (str) Linux app categories
# linux.app_categories = Network;AudioVideo;

# (str) Linux app keywords
# linux.app_keywords = downloader;youtube;video;audio;

# (str) Linux app startup notify
# linux.app_startup_notify = false

# (str) Linux app terminal
# linux.app_terminal = false

# (str) Linux app type
# linux.app_type = Application

# (str) Linux app icon
# linux.icon = %(source.dir)s/data/icon.png

# (str) Linux desktop file
# linux.desktop = %(source.dir)s/data/brothers.desktop

# (str) Linux app name
# linux.app_name = Brothers 4.0

# (str) Linux app version
# linux.app_version = 4.0.0

# (str) Linux app author
# linux.app_author = Brothers

# (str) Linux app comment
# linux.app_comment = YouTube Downloader

# (str) Linux app categories
# linux.app_categories = Network;AudioVideo;

# (str) Linux app keywords
# linux.app_keywords = downloader;youtube;video;audio;

# (str) Linux app startup notify
# linux.app_startup_notify = false

# (str) Linux app terminal
# linux.app_terminal = false

# (str) Linux app type
# linux.app_type = Application

# (str) Linux app icon
# linux.icon = %(source.dir)s/data/icon.png

# (str) Linux desktop file
# linux.desktop = %(source.dir)s/data/brothers.desktop

# (str) Linux app name
# linux.app_name = Brothers 4.0

# (str) Linux app version
# linux.app_version = 4.0.0

# (str) Linux app author
# linux.app_author = Brothers

# (str) Linux app comment
# linux.app_comment = YouTube Downloader

# (str) Linux app categories
# linux.app_categories = Network;AudioVideo;

# (str) Linux app keywords
# linux.app_keywords = downloader;youtube;video;audio;

# (str) Linux app startup notify
# linux.app_startup_notify = false

# (str) Linux app terminal
# linux.app_terminal = false

# (str) Linux app type
# linux.app_type = Application

# (str) Linux app icon
# linux.icon = %(source.dir)s/data/icon.png

# (str) Linux desktop file
# linux.desktop = %(source.dir)s/data/brothers.desktop

# (str) Linux app name
# linux.app_name = Brothers 4.0

# (str) Linux app version
# linux.app_version = 4.0.0

# (str) Linux app author
# linux.app_author = Brothers

# (str) Linux app comment
# linux.app_comment = YouTube Downloader

# (str) Linux app categories
# linux.app_categories = Network;AudioVideo;

# (str) Linux app keywords
# linux.app_keywords = downloader;youtube;video;audio;

# (str) Linux app startup notify
# linux.app_startup_notify = false

# (str) Linux app terminal
# linux.app_terminal = false

# (str) Linux app type
# linux.app_type = Application

# (str) Linux app icon
# linux.icon = %(source.dir)s/data/icon.png

# (str) Linux desktop file
# linux.desktop = %(source.dir)s/data/brothers.desktop

# (str) Linux app name
# linux.app_name = Brothers 4.0

# (str) Linux app version
# linux.app_version = 4.0.0

# (str) Linux app author
# linux.app_author = Brothers

# (str) Linux app comment
# linux.app_comment = YouTube Downloader

# (str) Linux app categories
# linux.app_categories = Network;AudioVideo;

# (str) Linux app keywords
# linux.app_keywords = downloader;youtube;video;audio;

# (str) Linux app startup notify
# linux.app_startup_notify = false

# (str) Linux app terminal
# linux.app_terminal = false

# (str) Linux app type
# linux.app_type = Application

# (str) Linux app icon
# linux.icon = %(source.dir)s/data/icon.png

# (str) Linux desktop file
# linux.desktop = %(source.dir)s/data/brothers.desktop

# (str) Linux app name
# linux.app_name = Brothers 4.0

# (str) Linux app version
# linux.app_version = 4.0.0

# (str) Linux app author
# linux.app_author = Brothers

# (str) Linux app comment
# linux.app_comment = YouTube Downloader

# (str) Linux app categories
# linux.app_categories = Network;AudioVideo;

# (str) Linux app keywords
# linux.app_keywords = downloader;youtube;video;audio;

# (str) Linux app startup notify
# linux.app_startup_notify = false

# (str) Linux app terminal
# linux.app_terminal = false

# (str) Linux app type
# linux.app_type = Application

# (str) Linux app icon
# linux.icon = %(source.dir)s/data/icon.png

# (str) Linux desktop file
# linux.desktop = %(source.dir)s/data/brothers.desktop

# (str) Linux app name
# linux.app_name = Brothers 4.0

# (str) Linux app version
# linux.app_version = 4.0.0

# (str) Linux app author
# linux.app_author = Brothers

# (str) Linux app comment
# linux.app_comment = YouTube Downloader

# (str) Linux app categories
# linux.app_categories = Network;AudioVideo;

# (str) Linux app keywords
# linux.app_keywords = downloader;youtube;video;audio;

# (str) Linux app startup notify
# linux.app_startup_notify = false

# (str) Linux app terminal
# linux.app_terminal = false

# (str) Linux app type
# linux.app_type = Application