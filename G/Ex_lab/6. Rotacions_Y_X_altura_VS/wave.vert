#version 330 core

layout (location = 0) in vec3 vertex;
layout (location = 2) in vec3 color;

out vec4 frontColor;

uniform mat4 modelViewProjectionMatrix;

uniform float time;
uniform float amp = 0.5;
uniform float freq = 0.25;

const float pi = 3.141592;

//estaaaa maaaal
void main()
{
    float alpha = amp * 2*pi * sin(vertex.y);
    
    mat3 rotacioY = mat3 (
        vec3(1, 0, 0), 
        vec3(0, cos(alpha), -sin(alpha)), 
        vec3(0, sin(alpha), cos(alpha)));
    
    vec3 V = rotacioY * vertex * time * freq;
    
    frontColor = vec4(color,1.0);
    
    gl_Position = modelViewProjectionMatrix * vec4(V, 1.0);
}
 
