package com.tkyaji.cordova;

import android.net.Uri;
import android.util.Base64;
import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Pattern;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import org.apache.cordova.CordovaPlugin;
import org.apache.cordova.CordovaResourceApi.OpenForReadResult;
import org.apache.cordova.LOG;

public class DecryptResource extends CordovaPlugin {
    private static final String CRYPT_IV = "WIU8k71fDAspR8Ie";
    private static final String CRYPT_KEY = "nFwsAczxEZAs1QPF1lfA5eOWPg2TgvhF";
    private static final String[] EXCLUDE_FILES = new String[0];
    private static final String[] INCLUDE_FILES = {"\\.(htm|html|js|css)$"};
    private static final String TAG = "DecryptResource";

    public Uri remapUri(Uri uri) {
        if (uri.toString().indexOf("/+++/") > -1) {
            return toPluginUri(uri);
        }
        return uri;
    }

    public OpenForReadResult handleOpenForRead(Uri uri) throws IOException {
        String uriStr = fromPluginUri(uri).toString().replace("/+++/", "/").split("\\?")[0];
        OpenForReadResult readResult = this.webView.getResourceApi().openForRead(Uri.parse(uriStr), true);
        if (!isCryptFiles(uriStr)) {
            return readResult;
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(readResult.inputStream));
        StringBuilder strb = new StringBuilder();
        while (true) {
            String line = br.readLine();
            if (line == null) {
                break;
            }
            strb.append(line);
        }
        br.close();
        byte[] bytes = Base64.decode(strb.toString(), 0);
        LOG.m0d(TAG, "decrypt: " + uriStr);
        ByteArrayInputStream byteInputStream = null;
        try {
            SecretKeySpec secretKeySpec = new SecretKeySpec(CRYPT_KEY.getBytes("UTF-8"), "AES");
            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            cipher.init(2, secretKeySpec, new IvParameterSpec(CRYPT_IV.getBytes("UTF-8")));
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            bos.write(cipher.doFinal(bytes));
            byteInputStream = new ByteArrayInputStream(bos.toByteArray());
        } catch (Exception ex) {
            LOG.m3e(TAG, ex.getMessage());
        }
        return new OpenForReadResult(readResult.uri, byteInputStream, readResult.mimeType, readResult.length, readResult.assetFd);
    }

    private boolean isCryptFiles(String uri) {
        String checkPath = uri.replace("file:///android_asset/www/", "");
        if (hasMatch(checkPath, INCLUDE_FILES) && !hasMatch(checkPath, EXCLUDE_FILES)) {
            return true;
        }
        return false;
    }

    private boolean hasMatch(String text, String[] regexArr) {
        for (String regex : regexArr) {
            if (Pattern.compile(regex).matcher(text).find()) {
                return true;
            }
        }
        return false;
    }
}