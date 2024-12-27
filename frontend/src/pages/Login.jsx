import { Box, Button, Fieldset, Input, Stack } from "@chakra-ui/react"
import { Field } from "@chakra-ui/react"

function Login() {
    return (

        <>
            <section className="content-center flex h-screen">
                <div id="loginPage" className="flex justify-center items-center p-10 rounded-lg mx-auto">
                    <div className="content-center border-2 px-40 py-10 ">
                        <Stack align="center" gap="4">
                            <Button colorPalette="blue" className="p-4 " variant="surface">Login</Button>
                            <Button colorPalette="blue" className="p-4 ">Login</Button>
                            <Button colorPalette="red" className="p-4 " variant="outline">Login</Button>
                        </Stack>
                    </div>
                </div>
            </section>
        </>

    )
}

export default Login