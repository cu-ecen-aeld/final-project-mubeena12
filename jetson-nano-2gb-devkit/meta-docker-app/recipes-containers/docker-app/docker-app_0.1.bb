SUMMARY = "bitbake-layers recipe"
DESCRIPTION = "Recipe created by bitbake-layers"
LICENSE = "CLOSED"
python do_display_banner() {
    bb.plain("**************************************************");
    bb.plain("*                                                *");
    bb.plain("*  Docker-app recipe created by bitbake-layers   *");
    bb.plain("*                                                *");
    bb.plain("**************************************************");
}
SRC_URI = "file://Dockerfile \
           file://docker-compose.yml \
           file://app.py \
           file://requirements.txt \
           file://start-stop-webapp.sh \
           file://test-webapp.sh \
           "

S = "${WORKDIR}"

RDEPENDS_${PN} += "/bin/bash" 

# Add the docker-app application and any other files you need to install
FILES:${PN} += "${bindir}/docker-app"
FILES:${PN} += "${sysconfdir}/init.d/start-stop-webapp.sh"

inherit update-rc.d
INITSCRIPT_PACKAGES = "${PN}"
INITSCRIPT_NAME:${PN} = "start-stop-webapp.sh"

# Define the do_install task to copy files to the appropriate directories on the target system
do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${WORKDIR}/Dockerfile ${D}/usr/bin/
    install -m 0755 ${WORKDIR}/docker-compose.yml ${D}/usr/bin/
    install -m 0755 ${WORKDIR}/app.py ${D}/usr/bin/
    install -m 0755 ${WORKDIR}/requirements.txt ${D}/usr/bin/
    install -m 0755 ${WORKDIR}/test-webapp.sh ${D}/usr/bin/
    install -d ${D}${sysconfdir}/init.d/
    install -m 0755 ${S}/start-stop-webapp.sh ${D}${sysconfdir}/init.d/
    # Install other necessary files similarly
}

# You might need to specify dependencies or any other specific build instructions here

FILES_${PN} += " \
                ${bindir}\
		${libdir} \
		"

addtask display_banner before do_build
