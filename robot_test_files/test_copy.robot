*** Settings ***
Documentation     Test resource file
...               Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed enim metus, aliquet lacinia nisi eget, posuere sagittis libero. Proin vitae lacus sagittis, vehicula est sit amet, aliquet urna. Morbi metus ante, elementum in eros quis, maximus rhoncus augue. Integer faucibus est non tortor tristique laoreet. Ut eleifend sollicitudin mi eget consectetur. Donec id lacus sit amet urna luctus auctor rutrum eget neque. Curabitur pulvinar consectetur erat, ut dignissim enim tincidunt ut. Ut vestibulum purus ac orci sodales, a ultricies magna convallis. Mauris velit mi, accumsan sit amet nibh in, interdum lobortis lorem. Quisque feugiat turpis venenatis elementum ultrices. Quisque dignissim finibus pharetra. Praesent non congue lorem.
...               Vivamus lobortis felis vel finibus interdum. Fusce a quam risus. Donec faucibus orci id odio rutrum rutrum. Donec et vestibulum lacus, non vulputate leo. Ut sit amet ligula urna. Donec ut enim ligula. Vivamus libero mi, convallis quis aliquam ac, rhoncus vel odio. Sed enim sem, semper eget sollicitudin fringilla, scelerisque commodo dui. Praesent est augue, suscipit ac dictum id, rhoncus et lacus.
Library           String

*** Variables ***
${FOO}            BAR

*** Keywords ***
Empty Keyword

Keyword With Documentation
    [Documentation]    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed enim metus, aliquet lacinia nisi eget, posuere sagittis libero. Proin vitae lacus sagittis, vehicula est sit amet, aliquet urna. Morbi metus ante, elementum in eros quis, maximus rhoncus augue. Integer faucibus est non tortor tristique laoreet. Ut eleifend sollicitudin mi eget consectetur. Donec id lacus sit amet urna luctus auctor rutrum eget neque. Curabitur pulvinar consectetur erat, ut dignissim enim tincidunt ut. Ut vestibulum purus ac orci sodales, a ultricies magna convallis. Mauris velit mi, accumsan sit amet nibh in, interdum lobortis lorem. Quisque feugiat turpis venenatis elementum ultrices. Quisque dignissim finibus pharetra. Praesent non congue lorem.
    ...    Vivamus lobortis felis vel finibus interdum. Fusce a quam risus. Donec faucibus orci id odio rutrum rutrum. Donec et vestibulum lacus, non vulputate leo. Ut sit amet ligula urna. Donec ut enim ligula. Vivamus libero mi, convallis quis aliquam ac, rhoncus vel odio. Sed enim sem, semper eget sollicitudin fringilla, scelerisque commodo dui. Praesent est augue, suscipit ac dictum id, rhoncus et lacus.

Keyword With Tag
    [Tags]    Foo    Bar

Keyword With Arguments
    [Arguments]    ${Foo}    ${Bar}    ${Foo_Bar}=Foo_Bar

Keyword With Return
    [Return]    Foo

Keyword With All
    [Documentation]    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed enim metus, aliquet lacinia nisi eget, posuere sagittis libero. Proin vitae lacus sagittis, vehicula est sit amet, aliquet urna. Morbi metus ante, elementum in eros quis, maximus rhoncus augue. Integer faucibus est non tortor tristique laoreet. Ut eleifend sollicitudin mi eget consectetur. Donec id lacus sit amet urna luctus auctor rutrum eget neque. Curabitur pulvinar consectetur erat, ut dignissim enim tincidunt ut. Ut vestibulum purus ac orci sodales, a ultricies magna convallis. Mauris velit mi, accumsan sit amet nibh in, interdum lobortis lorem. Quisque feugiat turpis venenatis elementum ultrices. Quisque dignissim finibus pharetra. Praesent non congue lorem.
    ...    Vivamus lobortis felis vel finibus interdum. Fusce a quam risus. Donec faucibus orci id odio rutrum rutrum. Donec et vestibulum lacus, non vulputate leo. Ut sit amet ligula urna. Donec ut enim ligula. Vivamus libero mi, convallis quis aliquam ac, rhoncus vel odio. Sed enim sem, semper eget sollicitudin fringilla, scelerisque commodo dui. Praesent est augue, suscipit ac dictum id, rhoncus et lacus.
    [Tags]    Foo    Bar
    [Arguments]    ${Foo}    ${Bar}    ${Foo_Bar}=Foo_Bar
    [Return]    Foo

Not Filler1

Not Filler2

Not Filler3

Not Filler4

Not Filler5

Not Filler6

Not Filler7

Not Filler8

Not Filler9

Not Filler10

Not Filler11

Not Filler12

Not Filler13

