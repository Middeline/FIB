#version 330 core

in vec4 frontColor;
out vec4 fragColor;

in vec2 vtexCoord;

uniform float n = 8;

const vec2 C = vec2(0.5, 0.5);


void main() {
    float L = length(vtexCoord - C);
    float val = step(.2, L);
    fragColor = vec4(1, val, val, 1);
}
  
