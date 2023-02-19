#include <zip.h>

int main(int argc, char **argv) {
    // Open a zip archive for writing.
    int error;
    zip_t *zip = zip_open("archive.zip", ZIP_CREATE | ZIP_TRUNCATE, &error);
    if (!zip) {
        zip_error_t error;
        zip_error_init_with_code(&error, error);
        printf("Failed to create zip: %s\n", zip_error_strerror(&error));
        return -1;
    }

    // Add a folder to the zip archive.
    zip_source_t *source = zip_source_file(zip, "folder", 0, -1);
    if (!source) {
        printf("Failed to create source: %s\n", zip_strerror(zip));
        zip_close(zip);
        return -1;
    }
    zip_int64_t index = zip_add(zip, "folder.zip", source);
    if (index < 0) {
        printf("Failed to add to zip: %s\n", zip_strerror(zip));
        zip_source_free(source);
        zip_close(zip);
        return -1;
    }

    // Close the zip archive.
    if (zip_close(zip) == -1) {
        printf("Failed to close zip: %s\n", zip_strerror(zip));
        return -1;
    }

    return 0;
}