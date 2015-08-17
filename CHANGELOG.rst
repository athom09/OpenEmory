Release 1.3.1 Fedora Migration
------------------------------
Changes for Fedora 3.8


Release 1.3 - Pre Fedora Migration
----------------------------------
* Upgraded Django to 1.5
* Added downpage and maintenance banner
* Changed DC datastreams to be managed


Release 1.2.17 - Link Styles
----------------------------
* Wrap hyperlinks in sidebar


Release 1.2.16 - Connector
--------------------------
* Added bit and pices that are required for processing Symplectic objects


Release 1.2.15 - Bug Fixes
--------------------------
* Fixed footer Feedback link
* Changed Title to be required on OA form


Release 1.2.14 - Virtuals
-------------------------
* Modified Grant Proposal forom
* Updated Privacy Policy link
* Fixed file upload button when using FireFox


Release 1.2.13 - Menus Cleanup
------------------------------
* Updated Library Tools and Resources menu
* Updated Browse menus
* Updated Browse page titles
* Updated import_to_symplectic so that it matches the title based on percent of the title that matches.

Release 1.2.12 - Symplectic Elements
------------------------------------
* Updated import_to_symplectic with --rel flag to force update of author info on existing publications


<missing tag> - Symplectic Elements
-----------------------------------
* Added import-to-symplectic command to create OE Articles in Symplectic-Elements
* Remove ability for self-upload of Articles

Release 1.2.11 - Bug Fix
------------------------
* Fixed xml parsing error with ROMEO auto-complete


Release 1.2.10 - Supplemental Materials
---------------------------------------
* Added Supplemental Materials to edit form and article view
* Fixed big with deleting repeating fields


Release 1.2.9 - Odds and Ends
-----------------------------
* Admins no longer contribute to site stats
* New FlatPage Data Archiving is now viewable
* New branding images
* Resolved issue with missing spaces in indexdata

Release 1.2.8 - Reports
-----------------------
* Reports by Division, Author and Lead Author


Release 1.2.7 - OAI modifications
---------------------------------
* Modified add_to_oai and add_dc_ident commands to query Fedora directly instead of Solr and and unmap dc.relation.

Release 1.2.6 - Bug Fix and Enhancements
----------------------------------------
* Fixed issue with author ordering on initial add
* Fixed Harvest script so that it can harvest all available articles
* Added feature to Harvest script to allow query by date range
* Added feature to Harvest script to optionally show progress bar
* Added pagination to Harvest queue
* Modified code to use the --derive flag on ldap.find_user_by_email()

Release 1.2.5 - Bug Fix
-----------------------
* Restored dc identifiers to produce View on PubMed link

Release 1.2.4 - Captcha / Bug Fixes
-----------------------------------
* Several bug fixes
* Added Captcha to feedback form
* Removed non-functional RSS button
* Revised site statistics text

Release 1.2.3 - OAI
-------------------
* Added  ability for articles to be harvested by OAI



Release 1.2.2 - License and Rights Enhancements
-----------------------------------------------

* An authorized user can edit and save optional Creative Commons license information
  that is consistent with harvested content.

* When an OpenEmory Admin ingests a harvested record, any license information
   will be saved to the MODS metadata, for consistency with uploaded articles.

* A sysadmin or developer can run a manage command to update all  articles to save
  any license information in the MODS metadata.

* An uploaded article should not get an empty NLM XML datastream on ingest.

* An openEmory admin can add and edit available license choices through the
  admin panel so they can provide the user with the most relevant choices for licenses.

* When unauthenticated users view an uploaded article, they see the associated
  Creative Commons license information (if any), so that they are aware of any restrictions on reuse.

* An external system (such as DiscoverE) can harvest published OpenEmory articles
  via OAI-PMH, so that OpenEmory content can be made searchable and discoverable through other sources.

* A sysadmin or developer can run a migration script to make published articles available via OAI,
  so that existing records will be included in OAI-PMH harvests.

* A user viewing the "Submit an Article Page", sees updated text for "Mediated Deposit" section; also
  PREMIS message has been modified.

* An admin ingesting a harvested article, copyright information is populated into the MODs record.

* An author editing a record can add a copyright statement before the record is published .

* An admin editing any type of record can include a non-public optional administrative note.

* An admin editing any uploaded article, can record the date that rights research was conducted.


Release 1.2.1
-------------

* Bug fix: correct a conflict between flatpages url /publication/submit/ and
  article urls in publication views.


Release 1.2.0 - Search Engine optimization and bugfixes
-------------------------------------------------------

* When a user sees an OpenEmory article or profile in search engine
  results (such as Google), the article title or person's name will be
  listed first, so that the page content is more clear.

* A sysadmin or developer can configure whether Google Analytics
  should be used, so that Google Analytics can be enabled in production
  and disabled in staging or development sites.

* A sysadmin or developer can configure a Google site verification code,
  so that the site can verified and monitored with Google Webmaster Tools.

* When a user clicks "Save Changes" on the profile edit, they see some form of
  feedback to indicate that the page is saving or has been saved, so that they
  are not confused about whether clicking the button had any effect.

* If users follow an old link for one of the first 78 articles added to the
  site with the wrong pid, they will be redirected to the corrected pid so
  that they find the article and so that search engine page ranks transfer to
  the corrected articles.

* Bug fixes:

 - Fix save/ingest error on articles with too many authors.
 - Fix whitespace issues when displaying biography text on profile pages.
 - Fix formatting for degrees on profile edit form.
 - Fix for faculty autocomplete when no first name is indexed
 - Fix an error generating article citation when a keyword is set to `None`
 - Corrected sitemap.xml URL in robots.txt
 - Sectioned sitemaps out by type of content, added last-modified data for articles,
   and included flat pages

Release 1.1.2 - bugfixes
------------------------

* Fix a bug in profile edit that disables edit after saving changes.
* Fix a bug in article metadata edit that prevents editing authors in
  Firefox.

Release 1.1.1 - bugfixes and legal language
-------------------------------------------

* Always show Submit an Article link under For Authors
* Fix department formatting error in faculty profiles by department
* Use https for Share button script to eliminate browser security warning.
* Fix an incorrect HTML comment hiding some content on the article metadata
  edit form.
* Update legal language on article upload form, and allow admins to agree to
  legal terms for mediated upload in addition to author upload.

Release 1.1.0
-------------

* Admins can withdraw items.
* Admins can select articles to feature on the home page.
* Users can link to other sites on their profile page.
* Faculty members edit their profiles inline in the profile view.
* Disable profile photo upload and display while design issues are
  addressed.
* Autocomplete article Publisher from SHERPA/RoMEO, and use it to help
  admins assess publisher copyright policy.
* Add HTML head metadata to improve search engine accuracy.

Release 1.0.0 - Initial production release
------------------------------------------

This is our first release to the production website, with most basic
functionality implemented. It still contains a number of minor issues and
rough edges that need cleaning, so our first *publicized* release will be
1.1.0, but this is the first one aiming for installation on the real
production server.

* Users see site-themed search results to maintain design consistency across
  the site.
* Users see site-themed At A Glance page to maintain design consistency
  across the site.
* Users can access a site-themed (non-functional) feedback form, to maintain
  design consistency and so demo audiences understand what functionality will
  be available in future.
* When an authenticated user makes changes to an article, they see a
  site-themed message on the following page to alert them to the result of
  their action.
* Users see site-themed error messages for missing pages or pages they don't
  have permission to view, in order to reduce disorientation and help them
  continue using the site.
* Logged in faculty see a site-themed faculty dashboard to maintain design
  consistency across the site and so they can access their content and manage
  their profile from one page.
* Users see site-themed error messages when the server encounters an
  unexpected error to reduce disorientation and help them continue using the
  site.
* When a user clicks on the "Emory Open Access Policy" link under the About
  Us navigation tab, the page opens in a new window, so that they can return
  to OpenEmory more easily if desired.
* Logged in faculty and site admins see site-themed article edit and upload
  pages, for consistency and visual appeal.
* A logged-in user can upload a photo to their profile, so that they can
  customize their profile.
* Faculty members can see statistics for their own articles in order to
  gauge their personal research impact.
* Users editing the document edit form can edit authors without having to
  retype the entire list of authors in order, so that they can enter the
  author names to reflect the names on the article itself.
* An admin user viewing an article can click on a link to see the XML Fedora
  object audit trail.
* An admin user can see the provenance of a record, so that they can
  understand what repository the article came from (if harvested) or if the
  author deposited the article.
* A logged in site admin can access the harvest and review queues and the
  Django db-admin from a single Admin Dashboard so that they can perform or
  easily get to admin functions from one page.
* A site admin can create and maintain site-wide announcements, which are
  displayed to all users, to alert them of site-wide updates and planned
  downtime.
* When an embargo expires, the full text becomes visible and searchable
  within a day.
* In the edit profile page, faculty users can enter Research Interests in
  repeating fields consistent with the design of affiliation and degree
  inputs, so that all fields seem to have the same level of importance and so
  that they can easily enter phrases or single keywords.
* When a user is viewing their "edit profile" page , their entry for Center
  or Institute Affiliations will be autocompleted with suggestions using
  data entered by others, so that they have less confusion in completing the
  form and so that we can eventually sort articles by Center or Institute
  Affiliation.
* A user can import citations from OpenEmory into EndNote and Zotero, so that
  they can use articles in their work.
* A user can search a name in the search box and receive a list of people as
  well as a list of articles in their search results, so that they can search
  for faculty profiles within the same search interface as that used for
  articles.
* Faculty members can receive reports from OpenEmory quarterly, containing
  statistics about their articles, so that they can understand that people are
  looking at their items and build a connection with the site.
* When a user clicks "submit" on the Feedback Form, the form is sent to an
  appropraite admin email address so that administrators can process user
  feedback.
* Users can use a site UI feature to share articles via social media tools
  in order to increase easy sharing of site content.
* A faculty member using the document edit form sees a form with a clear
  layout of fields grouped logically, so that they can enter required
  information and optional information to their uploaded article.
* Users can browse articles by the School, Department or Division of their
  authors, so that they can see articles published by faculty members in
  various groups.
* Numerous additional minor design tweaks.

Release 0.7.0 - Polish and Prep
-------------------------------

The purpose of this milestone is to polish the faculty demo prototype, and
to begin to ready the site for template integration by adding features which
appear in the design.

**Internal prototype: Not for production release**

* When an author is editing article metadata, they can enter co-author names
  and select from suggestions (including name and division) from ESD data, so
  that they can add correct co-author names without knowing netIDs.
* When an author uploads an article, the file type is checked, so that users
  cannot upload non-PDF's.
* When a user is viewing information for an article, they can see the
  number of downloads and the number of views for that item, so that both
  anonymous users and authors can know the popularity of an article.
* When a user is viewing the footer of any page, they can see the total
  number of repository items, the total number of items downloaded, the number
  of items downloaded this year, the total number of members, and the number
  of members currently online, so that users can understand the size of the
  community and repository.
* On the Search Results page, a user can limit their original search by
  filters (facets), so that they can find records limited by Author, Journal,
  Subject, or Year.
* When a user clicks on a Subject, they are taken to a list of articles
  which share that subject, so that they can see research similar to the
  article they have found.
* On the Search Results page, a user can type into the "search within
  results..." box, so that they can search again within the results list.
* When a user clicks "OpenEmory at a Glance," they can see a page listing
  Top 10 Downloads and 10 Recent Additions, so that they can get a sense of
  what is being posted, and what is being downloaded, on the site.
* When a user clicks the "Browse by" navigation tab, they can choose
  Author, Subject, and Journal, so that they can browse the scholarship posted
  in Open Emory.
* When a logged-in user tries to leave the metadata edit form without saving,
  they see only one prompt to urge them to save, so that they can decide
  whether to save or leave the page.
* When an author is choosing a Subject on the metadata edit form, they can
  type into a text box with autofill and select the proper choice, so that
  they do not have to choose from an unwieldy list of subjects.
* When a user mouses over the "View Abstract" link in the item list view,
  they can see the abstract of the article, so that they can decide whether to
  pursue the article.
* When an anonymous user clicks the link to the PubMed version of an article,
  that version opens in a new tab or window, so that the user can easily
  differentiate and return to the Open Emory interface.
* When an admin ingests an article from the Harvest Queue, the article
  information changes to a link to the article and a link to edit the
  metadata, so that they can choose to view and/or review harvested articles
  from the same interface.
* Admin users can "publish" as well as "save," so that administrators can also
  change the status of a document to posted.


Release 0.6.0 - Faculty Demo
----------------------------

This milestone is intended to compile various tasks necessary for
producing a faculty demo site. Authors will be able to attach and
specify licensing and embargo information to deposited articles. Tasks
also include automatic recording and display of file information (size
and type) and assigning a permalink to each article, as well as
attaching a cover page to each article. Finally, the workflow for
saving and publishing articles will be fixed per feedback from the
Article Metadata milestone. User stories are somewhat disparate in
nature, but are required for producing a faculty demo.

**Demo -- Not for production release**


* When a logged in user initiates an article upload they are presented
  with a stub "Assent to Deposit" check form so demo audience members
  understand the feature as it will be implemented at a later date.
* When an author is editing article metadata, they can specify an
  optional embargo of 6 months, 18 months, or 1, 2, or 3 years (based
  on the publication date), so that they can elect to hide deposited
  items for a period of time of their own choosing, or mandated by
  their publisher.
* When a user other than the author or an admin views an embargoed
  record, they see a note about the embargo and the date the item will
  be available alongside the metadata instead of a full text link, so
  that they will understand why they can't download the full text.
* When a user is viewing an article that was harvested from an
  external source with licensing information (such as Creative
  Commons) attached, that license information is displayed with the
  article metadata, so the licensing information can be determined by
  anonymous users.
* When an Author ingests an article, it is assigned an ARK, so a
  permalink can be generated and the article can be persistently
  accessed.
* When an anonymous user views the PDF of an Open Emory article, a
  cover page precedes the article text, so that any anonymous user can
  identify the PDF as being from Open Emory.
* A user can save the metadata edit form without filling in all
  required fields, so that they can return to finish editing if they
  do not know the information contained in a required field.
* An Article owner can upload a PDF of the author agreement in the
  Metadata edit form so authors and site admins can maintain a
  definitive record of the publishing agreement.
* When an anonymous user views record information for an article, they
  see the file size and type in human readable format, so that they
  can understand what they're downloading before they do so.


Release 0.5.0 - Faculty Profiles
--------------------------------
This milestone is intended to create basic faculty profiles using Emory
Shared Data for basic directory information. Authors will also have the
opportunity to provide biographical and professional information to augment
their profiles. Authors may supply and edit some profile information at any
time. Authors who have instructed UTS to suppress their information will be
prompted to share some or all of this information through the Open Emory
interface.

**Internal prototype: Not for production release**

 * Unauthenticated users can visit profile pages for faculty with the
   faculty member's name, suffix, title, department, school, and list of
   uploaded or harvested articles, so that they learn more about the faculty
   member and publications.
 * When an unauthenticated user tries to visit a profile page for a
   non-faculty Emory user, they are told that no such profile exists, so
   that only Emory faculty members and manually-added users have public
   profiles.
 * When an authenticated user who isn't faculty or an admin tries to log in,
   their password is rejected and they are treated as if they do not have an
   account, so that only Emory faculty members can log in to the system.
 * When an anonymous user looks up a faculty member who is "directory
   suppressed" or "internet suppressed," they see the name and Open Emory
   data, but no other data imported from the directory, in order to maintain
   their privacy and abide by the university's privacy policies.
 * When a faculty member who is "directory suppressed" or "internet
   suppressed" is looking at their profile, they can choose to display their
   profile information as if they were not suppressed, so that their profile
   page can be populated and displayed.
 * An authenticated faculty user can add Degrees to their profile, including
   name of degree, institution, and year (with suggestions autofilled for
   the institution), so that they can describe themselves on their profile.
 * An authenticated faculty user can add a profile picture in gif, jpeg, or
   png format, to their own profile, so that they can display a photo when
   others view their profile. If no photo is uploaded, no placeholder image
   will be displayed.
 * An authenticated faculty user can add a biographical paragraph to their
   profile, so that they can describe their career in more detail.
 * An authenticated faculty user can add Positions to their profile, so that
   they can identify academic positions as director of an institute or
   program not supplied by UTS data.
 * An authenticated faculty user can add information to their profile on
   grants received, including granting agency, project title, and date (with
   autofilled suggestions for granting agency), so that they can describe
   their career in more detail.
 * An anonymous user can browse faculty profiles by school and department
   and division, so that they can identify Emory faculty members working in
   a particular field.
 * An admin user can edit the profile page of a faculty member or a
   pseudo-faculty member, so that admins can maintain and update and support
   users.
 * An admin user can manually create a profile page that looks like a
   faculty profile page for a non-faculty member, so that key administration
   advocates who do not have faculty status can nonetheless be added to the
   repository. That non-faculty user can edit the profile page as a faculty
   member would, so that they can display their information.


Release 0.4.0 - Article Metadata
--------------------------------
Attach searchable MODS descriptive metadata to articles. Authors can edit
this metadata as they are uploading the document. Further edits are the
responsibility of site admins.

**Internal prototype: Not for production release**

 * When an author successfully uploads an article, they see a form where
   they can edit article metadata before that article is visible to the
   public so that they can describe the item correctly before publishing it.
 * When editing article metadata, an author can specify free text values
   for: title, funding groups (multiple), journal title, journal publisher,
   volume, issue, page numbers, abstract, author notes, and keywords so they
   can describe the item correctly.
 * An author can click a "publish" button to save the metadata form and
   populate the record in the repository so that an item record can be
   displayed on the website. (Redirect to profile after successful publish).
 * When an author uploads an article, the type of resource is prepopulated
   as text, the file format as PDF, and the genre as article, so that the
   items are sharable and identifiable according to the requirements of
   MODS.
 * When editing article metadata, an author can specify co-authors by netid
   in order to credit colleagues and share metadata maintenance permission.
   The system will automatically assign these authors an Emory University
   institutional affiliation.
 * An author can specify a name (with an optional institutional affiliation)
   as a co-author instead of a netid so that they can include non-Emory
   co-authors. If they do, then the author name will not be linked to a
   profile.
 * An author can remove a co-author by deleting their name or netid and
   saving the form so that they can correct errors.
 * When editing article metadata, an author is required to specify whether
   an article is a pre-print, post-print, or final published version, so
   that users know which version of an authoritative peer-reviewed scholarly
   article they are downloading.
 * When editing article metadata, an author can specify the date of
   publication, with the year required and the month and day optional so
   that users can identify when the article was first published.
 * When editing article metadata, an author can specify a URL and/or DOI for
   the final published version of the article so that readers can access
   this version. The URL will be verified when the form is saved.
 * When editing article metadata, an author can specify additional URLs
   associated with the article (PubMed, other repository, etc) so that
   readers can find more information about it.
 * When editing article metadata, an author is required to select a text
   language from a drop-down menu in which the first option is English so
   that readers can decide whether to download the article. If no language
   is selected, the value will default to English.
 * When editing article metadata, an author can select subject headings
   taken from the ETD list of ProQuest research fields to aid searchability.
   Use same options and configuration available in ETD's, but hide numbers
   associated with field names.
 * When editing an article's funding group, journal title, journal
   publisher, keywords, or co-author affiliation, an author will be prompted
   with suggestions pulled from existing entries to those fields to improve
   normalization of data and reduce errors.
 * When an author is editing an article, they can click a "save" button to
   save their changes without publishing, so they can revise the record
   later.
 * When an author is editing an article and navigates away or closes the
   browser, they will see a warning if they have unsaved changes so they do
   not lose their work.
 * When an author logs in, they will see a list of any unpublished records
   on their profile page, so that they can edit and publish those items.
 * An anonymous user can view a published item record page, populated by the
   article's full metadata, so that they can decide whether to download it.
   This page should include a link to download the article as well as a
   permanent id (ARK/DOI) for the article.
 * When an author publishes an article, it will appear immediately in search
   and browse results and on any Emory author profile pages, so that the
   article can be viewed immediately.
 * An admin can view a list of recently published, un-reviewed items, so
   that they can select an item to review.
 * An admin can review and edit a published article, and mark it as
   "reviewed," for quality control on metadata. Once an article has been
   marked as "reviewed," the author can no longer edit it. Once an article
   has been marked as "reviewed," the review event will be recorded (date
   and user) and displayed for admins.
 * Admins will see an edit link for each article in every search, browse,
   and display view, so they can easily find and edit items from anywhere in
   the site.
 * A user browsing search results can see author names (rather than netID)
   to provide correct citation information.


Release 0.3.0 - Searching and Social
------------------------------------
Full-text searching of articles, and basic social features. Users can add
private tags to articles as well as use tagging systems to indicate their
own research interests.

**Internal prototype: Not for production release**

 * Anonymous users can search for words or phrases that appear anywhere in
   the full-text (PDF or PMC xml) or available metadata, in order to find
   relevant articles.
 * Anonymous users who search for articles can see results with relevancy
   score, title, author, date uploaded, and context highlighting, so that
   they can determine which articles to view.
 * An authenticated user can enter a public research interest on their
   profile page so that they can indicate their research interests (with
   auto-suggest based on existing public research interests).
 * An authenticated user entering a tag will be given suggestions from their
   own previous tags, so that they can be consistent in their tagging.
 * An unauthenticated user can view researcher interests on a user's profile
   pages and click on them to see other researchers with those interests.
 * An authenticated user looking at research interest page can click a
   button/link to add that research interest to their own profile.
 * Authenticated users viewing search results, profile listings, or a single
   article can add and edit private tags on any article so that they can
   refer to them later.
 * An authenticated user can view their own tags in a sidebar on any page so
   that they can access the articles they've tagged from anywhere in the
   site.
 * When an authenticated user clicks on one of their tags, they're brought
   to a list of articles with that tag so that they can select which article
   to view.


Release 0.2.0 - Harvesting
--------------------------
Harvest metadata from PubMed Central for articles written by Emory authors.
Do not publish this metadata immediately, but allow site admins to decide
whether or not to publish it.

**Internal prototype: Not for production release**

 * An admin user can designate other users as admin users in order to share
   the work of the maintaining the site.
 * When an admin user logs in, they are redirected to a queue of PubMed
   articles targeted for harvesting so that they can review items and select
   them for ingest.
 * Admin users looking at the harvesting queue have access to the metadata,
   the PubMed ID, a link to the PubMed entry and the associated user to
   enable selection for ingest.
 * When looking at an item in the harvesting queue, an admin user can click
   "ingest" to indicate that the item should be scheduled for harvest, and
   disappear from the harvesting queue.
 * When looking at an item in the harvesting queue, an admin user can click
   "ignore" to indicate that the item should be ignored & disappear from the
   harvesting queue.
 * An unauthenticated user can view items ingested from PubMed harvest on
   faculty profile pages with links to PubMed for content so they can read
   articles or metadata about articles by Emory authors.


Release 0.1.0 - Initial Prototype
---------------------------------
First working system prototype. Emory users can authenticate, ingest
content, and edit metadata for items. Unauthenticated users can view
ingested content and user profiles.

**Internal prototype: Not for production release**

 * An anonymous user enters the site through a landing page that includes a
   login box so they can start to upload.
 * An anonymous user can log into the site using Emory credentials to allow
   them to manage their own content. New Task
 * An authenticated user can use a web form to ingest a PDF into the repository
   to ensure enduring access and discoverability of that file.
 * An anonymous user can view any user's basic user profile page, which lists
   information about the user and the items they have uploaded so they can
   view and download those items.
 * An authenticated user is redirected to their profile, which includes a link
   for ingesting content to give them a personalized jumping-off "home"
   point for other functionality.
 * A file owner can create and edit bibliographic metadata about a file they
   have previously ingested to better identify it and to improve
   discoverability.
