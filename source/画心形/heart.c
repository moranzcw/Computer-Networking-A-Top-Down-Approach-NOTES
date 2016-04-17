#include <stdio.h>
#include <math.h>

float f(float x, float y, float z) 
{
    float a = x * x + 9.0f / 4.0f * y * y + z * z - 1;
    return a * a * a - x * x * z * z * z - 9.0f / 80.0f * y * y * z * z * z;
}

float h(float x, float z) 
{
    for (float y = 1.0f; y >= 0.0f; y -= 0.001f)
        if (f(x, y, z) <= 0.0f)
            return y;
    return 0.0f;
}

int main() 
{
    FILE* fp = fopen("./heart.ppm", "w");
    int sw = 512, sh = 512;
    fprintf(fp, "P3\n%d %d\n255\n", sw, sh);
    for (int sy = 0; sy < sh; sy++) {
        float z = 1.5f - sy * 3.0f / sh;
        for (int sx = 0; sx < sw; sx++) {
            float x = sx * 3.0f / sw - 1.5f;
            float v = f(x, 0.0f, z);
            int r = 0;
            if (v <= 0.0f) {
                float y0 = h(x, z);
                float ny = 0.001f;
                float nx = h(x + ny, z) - y0;
                float nz = h(x, z + ny) - y0;
                float nd = 1.0f / sqrtf(nx * nx + ny * ny + nz * nz);
                float d = (nx + ny - nz) / sqrtf(3) * nd * 0.5f + 0.5f;
                r = (int)(d * 255.0f);
            }
            fprintf(fp, "%d 0 0 ", r);
        }
        fputc('\n', fp);
    }
    fclose(fp);
}