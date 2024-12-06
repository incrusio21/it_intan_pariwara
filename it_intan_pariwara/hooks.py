app_name = "it_intan_pariwara"
app_title = "It Intan Pariwara"
app_publisher = "das"
app_description = "das"
app_email = "das@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/it_intan_pariwara/css/it_intan_pariwara.css"
# app_include_js = "/assets/it_intan_pariwara/js/it_intan_pariwara.js"

# include js, css files in header of web template
# web_include_css = "/assets/it_intan_pariwara/css/it_intan_pariwara.css"
# web_include_js = "/assets/it_intan_pariwara/js/it_intan_pariwara.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "it_intan_pariwara/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "it_intan_pariwara/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "it_intan_pariwara.utils.jinja_methods",
# 	"filters": "it_intan_pariwara.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "it_intan_pariwara.install.before_install"
# after_install = "it_intan_pariwara.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "it_intan_pariwara.uninstall.before_uninstall"
# after_uninstall = "it_intan_pariwara.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "it_intan_pariwara.utils.before_app_install"
# after_app_install = "it_intan_pariwara.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "it_intan_pariwara.utils.before_app_uninstall"
# after_app_uninstall = "it_intan_pariwara.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "it_intan_pariwara.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"it_intan_pariwara.tasks.all"
# 	],
# 	"daily": [
# 		"it_intan_pariwara.tasks.daily"
# 	],
# 	"hourly": [
# 		"it_intan_pariwara.tasks.hourly"
# 	],
# 	"weekly": [
# 		"it_intan_pariwara.tasks.weekly"
# 	],
# 	"monthly": [
# 		"it_intan_pariwara.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "it_intan_pariwara.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "it_intan_pariwara.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "it_intan_pariwara.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["it_intan_pariwara.utils.before_request"]
# after_request = ["it_intan_pariwara.utils.after_request"]

# Job Events
# ----------
# before_job = ["it_intan_pariwara.utils.before_job"]
# after_job = ["it_intan_pariwara.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"it_intan_pariwara.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

